/****************************** atomic model {{model_number}} *****************************************/

template<typename TIME>
class new_atomic_model_{{model_number}} : public empty_atomic_port<TIME> {{{{
public:
    new_atomic_model_{{model_number}}() = default;
}}}};

std::shared_ptr<cadmium::dynamic::modeling::model> atomic_model_{{model_number}} = cadmium::dynamic::translate::make_dynamic_atomic_model<new_atomic_model_{{model_number}}, {TIME}>();
/**************************************************************************************************/
