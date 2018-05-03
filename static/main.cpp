#include "empty_atomic.hpp"
#include "ports.hpp"

#include <iostream>

#include <cadmium/logger/common_loggers.hpp>
#include <cadmium/engine/pdevs_runner.hpp>
#include <cadmium/modeling/coupled_model.hpp>


/****************************** atomic model 0 *****************************************/
template<typename TIME>
class atomic_0 : empty_atomic<ports, TIME> {
	public:
    	atomic_0() = default;
};
/**************************************************************************************************/

/****************************** atomic model 1 *****************************************/
template<typename TIME>
class atomic_1 : empty_atomic<ports, TIME> {
	public:
    	atomic_1() = default;
};
/**************************************************************************************************/

/*************************** coupled model TOP *******************************************/
using top_submodels=cadmium::modeling::models_tuple<atomic_0, atomic_1>;
using top_ic=std::tuple<cadmium::modeling::IC<atomic_0, ports::out_0, atomic_1, ports::in_0>>;
using top_eic=std::tuple<>;
using top_eoc=std::tuple<>;
using top_input_ports=std::tuple<>;
using top_output_ports=std::tuple<>;

template<typename TIME>
using TOP_model=cadmium::modeling::coupled_model<TIME, top_input_ports, top_output_ports, top_submodels, top_eic, top_eoc, top_ic>;
/**************************************************************************************************/


int main() {

    cadmium::engine::runner<float, TOP_model> r(float(0));
    r.run_until(30000);
    
    return 0;
}
