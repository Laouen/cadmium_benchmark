#include "empty_atomic.hpp"
#include "ports.hpp"

#include <iostream>

#include <cadmium/logger/common_loggers.hpp>
#include <cadmium/engine/pdevs_dynamic_runner.hpp>
#include <cadmium/modeling/dynamic_coupled.hpp>
#include <cadmium/modeling/dynamic_model_translator.hpp>


cadmium::dynamic::modeling::IC makeic(std::string model_from, std::string model_to) {
		return cadmium::dynamic::translate::make_IC<ports::out_0, ports::in_0>(model_from, model_to);
}

std::shared_ptr<cadmium::dynamic::modeling::model> makeatomic() {
	return cadmium::dynamic::translate::make_dynamic_atomic_model<empty_atomic_port, float>();
}

int main() {

	/*************************** coupled model 1 *******************************************/
	cadmium::dynamic::modeling::Models sub_models_1;

	for (int i = 1; i < 10001; i++) {
		sub_models_1.push_back(makeatomic());
	}

	cadmium::dynamic::modeling::Ports iports_1 = {};
	cadmium::dynamic::modeling::Ports oports_1 = {};
	cadmium::dynamic::modeling::EICs eics_1 = {};
	cadmium::dynamic::modeling::EOCs eocs_1 = {};
	cadmium::dynamic::modeling::ICs ics_1;

	for (int i = 1; i < 10001; i++) {
		ics_1.push_back(makeic("atomic_model_0", "atomic_model_" + std::to_string(i)));
	}

	std::shared_ptr<cadmium::dynamic::modeling::coupled<float>> coupled_model_1 = std::make_shared<cadmium::dynamic::modeling::coupled<float>>(
	    "coupled_model_1",
	    sub_models_1,
	    iports_1,
	    oports_1,
	    eics_1,
	    eocs_1,
	    ics_1
	);
	/**************************************************************************************************/



    cadmium::dynamic::engine::runner<float, cadmium::logger::not_logger> r(coupled_model_1, float(0));
    r.run_until(30000);
    
    return 0;
}
