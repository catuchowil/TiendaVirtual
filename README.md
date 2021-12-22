# Proyecto : TIENDA VIRTUAL CODEFOX

#### DESCRIPCIÓN:

###### Codefox es un sistema de administración de una tienda virtual de equipos de tecnología de diferentes orígenes (país de fabricación) y marcas.

###### El sistema permite administrar todos los productos, clientes, vendedores y proveedores. Contando para ello formularios de acceso de los datos, consultas y listados de los ítems mencionados.

#### ESPECIFICACIÓN DE DESARROLLO
###### Para la construcción del proyecto genero cuatro aplicaciones dentro de un directorio al que llamo app, cada aplicación cuenta con su propia template, vistas, forms, urls, etc.
###### A nivel general utilizo una template y las demás template de cada aplicación hacen uso de la herencia de esta. 
###### Para que los formularios de carga de datos, puedan obtener los estilos que la template trae, utilizo una herramienta externa la cual instale por medio del gestor de paquetes pip y que se llama "widget_tweaks" (busqué documentación en internet para la implementación de la misma y es muy sencilla de instalar y utilizar).
###### Así mismo para la confección de modelos utilizo el tipo de campo choice, email, decimal y la relación entre tablas uno a muchos.
###### Nuevamente reitero que me guié de la documentación oficial de django y de otra documentación encontrada en internet.

#### FUNCIONALIDADES
###### El sistema cuenta con un menú Crear Nuevo donde se puede llamar al formulario de carga de cualquiera de las aplicaciones mencionadas.
###### Así mismo cuenta con un menú horizontal (que se puede acceder desde cualquiera de las páginas que se visite) donde se puede acceder a los listados generales y formulario de búsqueda (no realizado aún ya que no se pide en esta entrega) de productos, clientes, vendedores, y proveedores.
###### El menú cuenta con un acceso "Web Tienda" que no tiene funcionamiento aún, pero este acceso debería llevarnos a la página oficial de la tienda (tarea a realizar)
###### El ítem Inicio del menú principal nos lleva a la página Home del sistema de administración la cual cuenta con un carrusel y el acceso en pié de página de Acerca de... 
