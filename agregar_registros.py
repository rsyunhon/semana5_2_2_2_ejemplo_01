from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Ciudad
from crear_entidades import Estadio
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo Autor
#autor1 = Autor(nombre="José", apellido="Armijos", nacionalidad="ecuatoriana",
#        edad=40)
#autor2 = Autor(nombre="Sara", apellido="Benitez", nacionalidad="colombiana",
#        edad=20)
#autor3 = Autor(nombre="Pedro", apellido="Díaz", nacionalidad="peruana",
#        edad=35)
#autor4 = Autor(nombre="Mónica", apellido="Carrión", nacionalidad="ecuatoriana",
#        edad=25)

ciudad1= Ciudad(nombreCiudad="Quito", pais="Ecuador", poblacion=2215552)
ciudad2= Ciudad(nombreCiudad="Cuenca", pais="Ecuador", poblacion=815552)
ciudad3= Ciudad(nombreCiudad="Whashington DC", pais="EEUU", poblacion=14515552)

estadio1= Estadio(nombreEstadio="Monumental Banco Pichincha", direccionEstadio="ubicado en la avenida Barcelona, entre el barrio San Eduardo y el barrio Bellavista, al oeste de la ciudad de Guayaquil, Ecuador", capacidad=59283)
estadio2= Estadio(nombreEstadio="Modelo Alberto Spencer", direccionEstadio=" Avenida de Las Américas al norte de la ciudad de Guayaquil. ", capacidad=42000)
estadio3= Estadio(nombreEstadio="7 de Octubre", direccionEstadio="Está ubicado en la calle 20.ª y avenida Jaime Roldós de la ciudad de Quevedo", capacidad=15200)


# se agrega los objetos de tipo Autor a la sesión
# a la espera de un commit
session.add(ciudad1)
session.add(ciudad2)
session.add(ciudad3)
session.add(estadio1)
session.add(estadio2)
session.add(estadio3)


# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
