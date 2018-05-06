/*************************** coupled model TOP *******************************************/
using top_submodels=cadmium::modeling::models_tuple<{sub_models}>;
using top_ic=std::tuple<{ic}>;
using top_eic=std::tuple<>;
using top_eoc=std::tuple<>;
using top_input_ports=std::tuple<>;
using top_output_ports=std::tuple<>;

template<typename TIME>
using TOP_model=cadmium::modeling::coupled_model<TIME, top_input_ports, top_output_ports, top_submodels, top_eic, top_eoc, top_ic>;
/**************************************************************************************************/
