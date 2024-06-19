import sys
import os
import tupleSpaceConnection as sv

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("For commands: python main.py help")
        # Ou usar o ./quick_launch com as opções abaixo
        
    else:
        command = sys.argv[1]
        
        match command:
            
            case "help":
                print("help: Displays commands")
                print("test_client: Run a CLI client for testing")
                print("start_zk: Start the zookeeper server.")
                print("stop_zk: Stop the zookeeper server.")
                
            case "test_client":
                with open("zookeper_hosts.txt") as file:
                    line = file.readline()
                    while line:
                        if line[0] != "#":
                            hosts = line
                        line = file.readline()
                
                connection = sv.TupleSpaceConnection(hosts)
                # sv.test(connection)
                
                op = 0
                while op != 4:
                    print("1 - Read")
                    print("2 - Write")
                    print("3 - Get")
                    print("4 - Exit")
                    
                    op = int(input())
                    
                    match op:
                        
                        case 1:
                            print("Example query: INE5410 Fulano 8.5 75")
                            in_str = input()
                            query = in_str.strip().split()
                            
                            result = connection.read(query)
                            
                            print(result)
                        
                        case 2:
                            print("Example: INE5410 * 6 *")
                            in_str = input()
                            tuple_data = in_str.strip().split()
                            
                            connection.write(tuple_data)
                            
                        case 3:
                            print("Example query: INE2490 * * 75")
                            
                            in_str = input()
                            query = in_str.strip().split()
                            
                            result = connection.get(query)
                            
                            print(result)
                            
                        case 4:
                            print("EOF")
                                                        
                        case _:
                            continue

            case "start_zk":
                os.system("apache-zookeeper-3.9.2-bin/bin/zkServer.sh start")
            
            case "stop_zk":
                os.system("apache-zookeeper-3.9.2-bin/bin/zkServer.sh stop")
                
            case _:
                print("To see available commands: python main.py help")