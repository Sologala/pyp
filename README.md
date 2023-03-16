# pyp
pyp is a personal code library of `c++` and `python` about `image processing`,`improvement of some common tools`. 

# cpp

- `cmdline` is a simple but powerful argument parser library.
- `timer` can be used flexibly to statistic running time.
- `yaml` is forked from [mini-yaml](https://github.com/jimmiebergmann/mini-yaml) and enhanced with array parsing and some `marco` like `${CURRENT_FOLDER}`


## Install and Uninstall

<!-- **Caution** -->


<!-- The cpp library will be build and install to `${HOME}/.local/`. 
You can change it in `./CMakeLists.txt`

```cmake
set(CMAKE_INSTALL_PREFIX "$ENV{HOME}/.local/") 
``` -->

### build  and install 

```shell
./install.sh
```

### uninstall 
```shell
./uninstall.sh
```


### cmake usage 

```cmake 

find_package(pyp REQUIRED)

target_link_libraries(${YOUR_LIB}
    pyp::fmt
    pyp::timer
    pyp::yaml
    pyp::cmdline
)
```


# python
- `ObjectDetection` contains some python code fragments of darwing, bounddingbox format transforming  as well as dataset creating.

## install
```shell
python ./setup.py develop
```

## uninstall 
```shell
pip uninstall pyp
```


## NOTE:
[some loss function](https://github.com/TouchDeeper/TdLib/tree/dev/src/slam_tool/backend)
