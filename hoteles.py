import pandas as pd

hoteles =['Alua Bocaccio','Aluasun Continental Park','Aluason Torrenova','Caribbean Bay','Habana Bay','Linda','Mediterranean Bay','Palma Bay',
    'Ritort','Samos','Atlantic Park','Triton beach','Linda','Mll Mediterranean Bay Adults Only','Aguamarina I','Aguamarina II',
    'Cala Galdana','Sur Menorca','Almirante Ferragut','Atlantic','Coral Beach','Ereso','Es Pla','San Antonio','Invisa Figueral Resort','Invisa La Cala',
    'Altamadores','Altamar','Concorde','Occidental Las Canteras','Green Field','Koala Garden','Astoria','Blue Sea Costa Teguise Gardens','Alua Parque San Antonio',
    'Alua Tenerife','Aluasoul Orotava Valley','Catalonia Las Vegas','Checkin Concordia Playa','HC Hotel Magec','Marquesa','Parque Vacacional Eden',
    'Valle Orotava','Catalonia Punta del Rey','Panorámica Garden','Barceló Tenerife','Royal Suite','Chatur Costa Caleta','Hotel Royal Suite','Smy Tahona Fuerteventura',
    'Alua Golf Trinidad','Bahía Serena','Best Roquetas','Best Sabinal','El Palmeral','Best Mojacar','Ele Andarax','Portomagno',
    'Vertice Indalo Almeria','Chinasol','Toboso','Checkin Camino De Granada','Dunas de Doñana Golf Resort','Flamero','Gran Hotel del Coto','Pato Amarillo',
    'Ilunion Islantilla','Occidental Isla Cristina','Playacanela','Aluasoul Costa Málaga','Aluasun Costa Park','Marconfort Griego','Parasol Garden',
    'Puente Real','Aluasun Marbella Park','Globales Gardenia''Las Palmeras', 'Medplaya Bali','Medplaya Balmoral','Paraiso Beach','Ilunion Mijas',
    'Ilunion Calas De Conil','Ilunion Sancti Petri','Melia Atlantera','Puerto Sherry','Vertice Chipiona Mar','Nh Avenida Jerez','Condestable Iranzo',
    'Crisol Jardines De Córdoba','Exe Las Adelfas','Castillo','Catalonia Hispalis''Htop Amaika & Spa', 'Htop Calella Palace Family & Spa', 'Santa Mónica',
    'Htop Pineda Palace','Mercury','Ciudad de Mataro','Ibersol Sorra Dor', 'Luna Park Yoga & Spa','Exe Cristal Palace','Garbi Park', 
    'Gran Garbi', 'Htop Royal Star & Spa', 'Samba','Surf-Mar','Tossa Beach Center','Caleta Palace','Platja Park','Best Western P. Cmc Girona',
    'Best Da Vinci', 'Best Los Ángeles', 'Best Mediterráneo', 'Best San Diego', 'Calypso','Htop Molinos Park', 'Medplaya Pirámide Salou','Oasis Park',
    'Best Cambrils','La Rapita','Natura Park','Estival Park Silmar','Medplaya Pino Alto','Ciutat De Tarragona','Gaudi','Dominio de Benidorm con Acapulco', 'Benidorm East',
    'Brasil','Caballo de Oro','Cabana','Carlos I','Cuco','Dynastic' ,'Fiesta Park' ,'Gala Placidia' ,'Golden' ,'Gran Hotel Bali' ,'Jaime I',
    'Joya', 'Lido' ,'Los Álamos' ,'Magic Cristal Park' ,'Magic Rock Gardens' ,'Mareny Benidorm', 'Melina' ,'Mont Park' ,'Montesol' ,'Oasis Plaza', 
    'Olympus' ,'Port Vista Oro' ,'Poseidón Playa' , 'Poseidón Resort', 'Sol y Sombra' ,'Tropic Relax','Alone','Playas Torrevieja','Port Denia',
	'Villa Naranjo','Sun Palace Albir','Port Europa','Roca Esmeralda','Cap Negret' ,'Port Elche' ,'Port Alicante' ,'Aparthotel & Spa Acualandia', 
    'Gran Hotel Peñíscola', 'Aparthotel & Spa Acuazul', 'RH Casablanca Suites' , 'RH Don Carlos & Spa','Intur Orange' ,'RH Vinarós Playa' ,
    'Porto','RH Bayren Park','RH Gijón','Safari','Tres Anclas','Villa Luz','Sicania','Olympia','Port Feria','La Mirage','Aluason Doblemar',
    'Entremares','Izan Cavanna','Occidental Mar Menor','Allegro Murcia Azarbe','Miranda Suizo','Florida','Villa De Pinto','Equo Aranjuez','Axor Feria',
    'Pedro I De Aragon','Rey Sancho Ramírez','Albarracín','Civera','Reina Cristina','Mora','Eurostars Zaragoza','Eurostars Boston',
    'Exe Oviedo Centro','Arbeyal','Arha Villa De Suances','Torresport','Arha Santander','Arha Villa de Santoña','Arha Reserva Del Saja','Nh Ciudad Real',
    'Exe Cuenca', 'Guadalajara & Conference Center','Perales','Be Live City Center Talavera','Eurostars Toledo','Reina Victoria','Cuatro Postes',
    'Puerta De Gredos','Exe Puerta de Burgos','Corona de Castilla','Rey Arturo','Alda Mercado De Zamora','Alfonso Viii Soria','Ele Acueducto',
    'Leon Camino','Olid','Rey Sancho''Gran Hotel Corona Sol','Extremadura Hotel','Ilunion Golf Badajoz','Gran Hotel Corona Sol','Exe Auriense',
    'Exe Coruña','Mendez Nuñez','Ciudad De Compostela','Sancho Ramirez','Barcelo Costa Vasca','Occidental Bilbao','Unzaga Plaza','Ceuta Puerta De Africa','Ciudad De Haro'
]


