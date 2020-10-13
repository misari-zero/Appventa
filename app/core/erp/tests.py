from config.wsgi import *
from core.erp.models import Type, Employed

#LISTAR

# select * from Tabla
# query = Type.objects.all()
# print(query)

# insercion
# t = Type(id='5',name='Alksjdkjs23')
# t.id = 5
# t.name = 'Purekjas'
# t.save()

# edicion
#     t = Type.objects.get(pk=1)
#     t.name = 'Presidente'
#     t.save()

# eliminacion
# t = Type.objects.get(pk=1)
# t.delete()


obj = Employed.objects,filter(type_id=1, )

#obj = Type.objects.filter(name__icontains='presidente').query
for i in Type.objects.filter(name__endswith ='e'):
    print(i.name)