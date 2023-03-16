install_path=$1
rm -rf build
mkdir build
cd build
if [ $1 = "global" ]; then
    cmake ..
elif [ $1 = "local" ]; then
    cmake .. -DCMAKE_INSTALL_PREFIX=installed	
else
    cmake .. -DCMAKE_INSTALL_PREFIX=../$1
fi
make install 
cd ..
