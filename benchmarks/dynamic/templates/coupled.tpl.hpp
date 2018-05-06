/*************************** coupled model {{model_number}} *******************************************/

cadmium::dynamic::modeling::Models sub_models_{{model_number}} = {{{{
	{{sub_models}}
}}}};
cadmium::dynamic::modeling::Ports iports_{{model_number}} = {{{{}}}};
cadmium::dynamic::modeling::Ports oports_{{model_number}} = {{{{}}}};
cadmium::dynamic::modeling::EICs eics_{{model_number}} = {{{{}}}};
cadmium::dynamic::modeling::EOCs eocs_{{model_number}} = {{{{}}}};
cadmium::dynamic::modeling::ICs ics_{{model_number}} = {{{{
	{{ic}}
}}}};

std::shared_ptr<cadmium::dynamic::modeling::coupled<{TIME}>> coupled_model_{{model_number}} = std::make_shared<cadmium::dynamic::modeling::coupled<{TIME}>>(
    "coupled_model_{{model_number}}",
    sub_models_{{model_number}},
    iports_{{model_number}},
    oports_{{model_number}},
    eics_{{model_number}},
    eocs_{{model_number}},
    ics_{{model_number}}
);
/**************************************************************************************************/
