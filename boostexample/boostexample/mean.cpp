#include <boost/python.hpp>

using namespace boost::python;

struct Mean
{
    double compute(list numbers) {
        double result = 0.0;
        for (size_t i = 0; i < len(numbers); ++i) {
            result += extract<double>(numbers[i]);
        }
        return result / (float) len(numbers);
    }
};

BOOST_PYTHON_MODULE(mean)
{
    class_<Mean>("Mean")
        .def("compute", &Mean::compute)
    ;
};
