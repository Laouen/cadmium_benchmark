/*************************** coupled model {model_number} *******************************************/
using submodels_{model_number}=cadmium::modeling::models_tuple<{sub_models}>;
using ic_{model_number}=std::tuple<{ic}>;
using eic_{model_number}=std::tuple<>;
using eoc_{model_number}=std::tuple<>;

template<typename TIME>
using coupled_{model_number}=cadmium::modeling::coupled_model<TIME, ports::input_ports, ports::output_ports, submodels_{model_number}, eic_{model_number}, eoc_{model_number}, ic_{model_number}>;
/**************************************************************************************************/
