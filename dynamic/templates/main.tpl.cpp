
int main() {{{{

    cadmium::dynamic::engine::runner<{TIME}, cadmium::logger::not_logger> r(coupled_model_{{model_number}}, {TIME}(0));
    r.run_until(30000);
    
    return 0;
}}}}