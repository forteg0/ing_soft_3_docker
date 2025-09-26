Se parte de una imagen ligera de phyton, se establece /app como carpeta de trabajo, COPY y RUN para instalar dependencias, copia el codigo tambien y se setea el puerto, el CMD para dar inicio.

En  el docker-compose levanta dos entornos completos separados en la misma máquina: QA y Producción. Cada entorno tiene su propia base MySQL y su aplicación, con puertos distintos para evitar conflictos. Además, los volúmenes aseguran que los datos no se pierdan al reiniciar los contenedores y depends_on garantiza que las aplicaciones no intenten conectarse a la base antes de que esta esté lista.

elegimos mysql, simplemente porque era una BD conocida que usamos en distintas materias. pero ademas MySQL cuenta con imágenes oficiales en Docker Hub, lo que facilita su despliegue y actualización.

las variables de entorno son 2: la url de la BD y el environment, cada ENV tiene su propia BD que es un volume de Mysql
