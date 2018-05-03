/****************************************** ports  ************************************************/
struct ports {{

	/* output por defs */
    {output_ports_definitions}

	/* input por defs */
    {input_ports_definitions}

	/* output por tuple */
    using input_ports=std::tuple<{input_port_names}>;
    
	/* input por tuple */
    using output_ports=std::tuple<{output_port_names}>;
}};
/**************************************************************************************************/
