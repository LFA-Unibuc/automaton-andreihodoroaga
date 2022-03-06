class Automaton:

    def __init__(self, config_file):
        self.config_file = config_file

        automaton = {"sigma": [], "states": [], "transitions": []}
        # create a dictionary containing sigma, states and transitions
        with open(self.config_file) as f:
            while len(automaton["sigma"]) == 0\
              or len(automaton["states"]) == 0 or len(automaton["transitions"]) == 0:
                line = f.readline().strip()
                section = line.lower().split(":", maxsplit=1)[0].strip()
                # ignore comments
                if line[0] == "#":
                    continue
                # check if a section follows
                elif section in automaton.keys():
                    while line.lower() != "end":
                        line = f.readline().strip()
                        if "..." not in line and "end" not in line.lower():
                            automaton[section].append(line)
        # refactor states
        automaton["states"] = [tuple([s.strip() for s in state.split(",")]) for state in automaton["states"]]

        self.automaton = automaton
        print(automaton)

    def validate(self):
        # check for unique start state and final state
        states_info = [state[1] if len(state) > 1 else "" for state in self.automaton["states"]]
        if states_info.count("S") > 1:
            raise Exception("Only one starting state allowed!")

        # check transitions
        for transition in self.automaton["transitions"]:
            state1, word, state2 = [t.strip() for t in transition.split(",")]
            valid_states = [state[0] for state in self.automaton["states"]]

            if state1 not in valid_states or state2 not in valid_states or word not in self.automaton["sigma"]:
                raise Exception("Transition contains invalid words or states!")
        return True

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        pass
    

if __name__ == "__main__":
    a = Automaton('input.txt')
    print(a.validate())
