#ifndef ATOMIC_TEST_DYNAMIC_HPP
#define ATOMIC_TEST_DYNAMIC_HPP

#include <string>
#include <fstream>

#include "ports.hpp"

#include <cadmium/modeling/ports.hpp>
#include <cadmium/modeling/message_bag.hpp>

using namespace std;
using namespace cadmium;

template<class PORTS, class TIME>
class empty_atomic {
public:

    using input_ports=typename PORTS::input_ports;
    using output_ports=typename PORTS::output_ports;

    using output_bags=typename make_message_bags<output_ports>::type;
    using input_bags=typename make_message_bags<input_ports>::type;

    using state_type = int;

    state_type state;

    empty_atomic() = default;

    void internal_transition() {
    }

    void external_transition(TIME e, input_bags mbs) {
    }

    void confluence_transition(TIME e, input_bags mbs) {
        
    }

    output_bags output() const {
        output_bags bags;
        return bags;
    }

    TIME time_advance() const {
        return TIME();
    }

    friend std::ostream& operator<<(std::ostream& os, const typename empty_atomic<PORTS,TIME>::state_type& s) {
        os << "empty_atomic";
        return os;
    }
};

template<typename TIME>
class empty_atomic_port : public empty_atomic<ports, TIME> {
public:
    empty_atomic_port() = default;
};

#endif //ATOMIC_TEST_DYNAMIC_HPP