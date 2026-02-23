# git_prueba
# 🛠️ Guía de Compilación para Colaboradores

Si quieres usar este paquete en tu computadora, sigue estos pasos exactos:

### 1. Ubicación del Workspace
Primero, asegúrate de estar en la carpeta de código (`src`) de tu espacio de trabajo de ROS 2. Si no tienes uno, créalo así:
```bash
mkdir -p ~/first_ws/src
cd ~/first_ws/src

#2
git clone [https://github.com/Armevc09/git_prueba.git](https://github.com/Armevc09/git_prueba.git)

#3
cd ..
colcon build --packages-select git_prueba

#4
ros2 run git_prueba saludo

