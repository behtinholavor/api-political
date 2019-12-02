from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# db_connect = create_engine('sqlite:///S:/political.db')
db_connect = create_engine('sqlite:///../db/political.db')
app = Flask(__name__)
api = Api(app)


# http://localhost:5000/political/value/614.90/year/2017
# http://localhost:5000/political/value/614.30/year/2017
# http://localhost:5000/political/value/614.10/year/2017

class All(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from vw_parlamentar")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class AllYear(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from vw_parlamentar_ano")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class YearById(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from vw_parlamentar_ano where Ano = '{0}' ".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class AllMonth(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from vw_parlamentar_mes")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class MonthById(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from vw_parlamentar_mes where Mes = '{0}' ".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class Political(Resource):
    def get(self, value, year):
        conn = db_connect.connect()
        sql = "select * from vw_parlamentar_valor where Ano = '{0}' and Valor <= '{1}' ".format(year, value)
        query = conn.execute(sql)
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        json = jsonify(result).get_json()
        row = json[0]

        max_value = round(float(row['Maximo']), 2)
        min_value = round(float(row['Minimo']), 2)
        avg_value = round(float(row['Valor']), 2)
        arg_value = round(float(value), 2)
        year_value = int(year)

        if avg_value == arg_value:
            msg = 'Parlamentar obteve gastos na média!'
        elif avg_value < arg_value:
            msg = 'Parlamentar obteve gastos maiores do que a média!'
        elif avg_value > arg_value:
            msg = 'Parlamentar obteve gastos menores do que a média!'

        res = jsonify({'Year': year_value, 'Average': avg_value, 'Value': arg_value, 'Message': msg})
        return res;


class Spender(Resource):
    def get(self, limit):
        conn = db_connect.connect()
        sql = "select * from vw_parlamentar_spender limit {0}".format(limit)
        query = conn.execute(sql)
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result);


class Sparer(Resource):
    def get(self, limit):
        conn = db_connect.connect()
        sql = "select * from vw_parlamentar_sparer where Liquido > 0 limit {0}".format(limit)
        query = conn.execute(sql)
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result);


api.add_resource(All, '/all')
api.add_resource(AllYear, '/all/year')
api.add_resource(YearById, '/all/year/<id>')
api.add_resource(AllMonth, '/all/month')
api.add_resource(MonthById, '/all/month/<id>')
api.add_resource(Political, '/political/value/<value>/year/<year>')
api.add_resource(Spender, '/political/spender/<limit>')
api.add_resource(Sparer, '/political/sparer/<limit>')

if __name__ == '__main__':
    app.run()
