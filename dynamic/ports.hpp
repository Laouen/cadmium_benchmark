#ifndef PORTS_TEST_CPP
#define PORTS_TEST_CPP

#include <cadmium/modeling/ports.hpp>

/****************************************** ports  ************************************************/
struct ports {

	/* output por defs */
    struct out_0: public cadmium::out_port<int>{};

	/* input por defs */
    struct in_0: public cadmium::in_port<int>{};

	/* output por tuple */
    using input_ports=std::tuple<in_0>;
    
	/* input por tuple */
    using output_ports=std::tuple<out_0>;
};
/**************************************************************************************************/


#endif //PORTS_TEST_CPP
