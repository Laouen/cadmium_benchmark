
int main() {{

    cadmium::engine::runner<{TIME}, TOP_model> r({TIME}(0));
    r.run_until(30000);
    
    return 0;
}}