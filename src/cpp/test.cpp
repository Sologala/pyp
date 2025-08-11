
#include <pybind11/pybind11.h>
#include "dynamic_lib.h"


namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
  m.doc() = R"pbdoc(
      Pybind11 example plugin
      -----------------------
      .. currentmodule:: python_example
      .. autosummary::
         :toctree: _generate
         add
         subtract
  )pbdoc";

  m.def("add", &func, R"pbdoc(
      Add two numbers
      Some other explanation about the add function.
  )pbdoc");

  m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
      Subtract two numbers
      Some other explanation about the subtract function.
  )pbdoc");
}
