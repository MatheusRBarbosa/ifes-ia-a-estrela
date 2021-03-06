import sys
from tools import *
from star import *

def main():
    if len(sys.argv) >= 2:
        print_arrow_style = False;
        map = read_text_file(sys.argv[1])


        if len(sys.argv) == 6 or len(sys.argv) == 7:
            initial_node = tuple([int(sys.argv[2]), int(sys.argv[3])])
            final_node = tuple([int(sys.argv[4]), int(sys.argv[5])])

            if len(sys.argv) == 7 and sys.argv[6] == "--arrows":
                print_arrow_style = True
        else:
            initial_node = input("Entre com o x e y do nó inicial. Ex: 0 3: ")
            initial_node = tuple(int(x) for x in initial_node.split(" "))
            final_node = input("Entre com o x e y do nó final. Ex: 0 3: ")
            final_node = tuple(int(x) for x in final_node.split(" "))

            if len(sys.argv) == 3 and sys.argv[2] == "--arrows":
                print_arrow_style = True

        if (check_inputs([initial_node, final_node], map)):
            print("=== Matriz inicial ===")
            print_map(map, initial_node, final_node)

            result = star_main(map, initial_node, final_node)
            
            print("=== Matriz com resultado ===")
            print_map(map, initial_node, final_node, result, print_arrow_style)
    
    else:
        print("Erro! Favor informar arquivo do mapa")

main()