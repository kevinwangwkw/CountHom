#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "hom.hh"

using namespace pybind11;

PYBIND11_MODULE(homlib, m) {
    m.doc() = "EEfficient Graph Homomorphism Counting Algorithm";
    class_<Graph>(m, "Graph")
        .def(init<int>())
        .def("addEdge", &Graph::addEdge);
    m.def("hom", &hom<double>, "homomorphism counting function (double)");
}
