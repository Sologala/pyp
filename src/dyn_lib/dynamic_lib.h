#pragma  once
//
// 导出宏：Windows 下需要显式声明导出/导入
#ifdef _WIN32
  #ifdef DYNAMIC_LIB_EXPORTS  // 编译动态库时定义，用于导出
    #define DYNAMIC_LIB_API __declspec(dllexport)
  #else  // 其他模块使用时，用于导入
    #define DYNAMIC_LIB_API __declspec(dllimport)
  #endif
#else
  #define DYNAMIC_LIB_API  // 非 Windows 平台不需要
#endif


DYNAMIC_LIB_API  int func(int a, int b );
