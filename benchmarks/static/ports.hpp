#ifndef PORTS_TEST_CPP
#define PORTS_TEST_CPP

#include <cadmium/modeling/ports.hpp>

/****************************************** ports  ************************************************/
struct ports {

	/* output por defs */
    struct out_0: public cadmium::out_port<int>{};
	struct out_1: public cadmium::out_port<int>{};
	struct out_2: public cadmium::out_port<int>{};
	struct out_3: public cadmium::out_port<int>{};
	struct out_4: public cadmium::out_port<int>{};
	struct out_5: public cadmium::out_port<int>{};
	struct out_6: public cadmium::out_port<int>{};
	struct out_7: public cadmium::out_port<int>{};
	struct out_8: public cadmium::out_port<int>{};
	struct out_9: public cadmium::out_port<int>{};

	/* input por defs */
    struct in_0: public cadmium::in_port<int>{};
	struct in_1: public cadmium::in_port<int>{};
	struct in_2: public cadmium::in_port<int>{};
	struct in_3: public cadmium::in_port<int>{};
	struct in_4: public cadmium::in_port<int>{};
	struct in_5: public cadmium::in_port<int>{};
	struct in_6: public cadmium::in_port<int>{};
	struct in_7: public cadmium::in_port<int>{};
	struct in_8: public cadmium::in_port<int>{};
	struct in_9: public cadmium::in_port<int>{};

	/* output por tuple */
    using input_ports=std::tuple<in_0,in_1,in_2,in_3,in_4,in_5,in_6,in_7,in_8,in_9>;
    
	/* input por tuple */
    using output_ports=std::tuple<out_0,out_1,out_2,out_3,out_4,out_5,out_6,out_7,out_8,out_9>;
};
/**************************************************************************************************/

