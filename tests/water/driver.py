import mdi
from mdi import MDI_NAME_LENGTH, MDI_COMMAND_LENGTH
import sys

iarg = 1
while iarg < len(sys.argv):
    arg = sys.argv[iarg]

    if arg == "-mdi":
        # Initialize MDI
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -mdi option not found")
        mdi.MDI_Init(sys.argv[iarg+1])
        iarg += 1
    else:
        raise Exception("Unrecognized argument")

    iarg += 1

# Connect to the engine
comm = mdi.MDI_Accept_Communicator()

# Get the name of the engine, which will be checked and verified at the end
mdi.MDI_Send_Command("<NAME", comm)
initial_name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)
print("Engine name: " + str(initial_name))

# Get the node name
mdi.MDI_Send_Command("<@", comm)
node_name = mdi.MDI_Recv(mdi.MDI_COMMAND_LENGTH, mdi.MDI_CHAR, comm)
print("Node name: " + str(node_name))

##############
print("AAA")
mdi.MDI_Send_Command("@INIT_MD", comm)
print("BBB")


# Verify that the engine is still responsive
mdi.MDI_Send_Command("<NAME", comm)
final_name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)
print("Final engine name: " + str(final_name))

mdi.MDI_Send_Command("<NATOMS", comm)
natoms = mdi.MDI_Recv(1, mdi.MDI_INT, comm)
print("NATOMS: " + str(natoms))

for iteration in range(20):
    mdi.MDI_Send_Command("@COORDS", comm)

    mdi.MDI_Send_Command("<COORDS", comm)
    coords = mdi.MDI_Recv(3 * natoms, mdi.MDI_DOUBLE, comm)
    #print("   COORDS: " + str(coords))

    mdi.MDI_Send_Command(">COORDS", comm)
    mdi.MDI_Send(coords, 3 * natoms, mdi.MDI_DOUBLE, comm)

    #print("Iteration: " + str(iteration))
    mdi.MDI_Send_Command("@FORCES", comm)

    #mdi.MDI_Send_Command("<@", comm)
    #node_name = mdi.MDI_Recv(mdi.MDI_COMMAND_LENGTH, mdi.MDI_CHAR, comm)
    #print("   NODE: " + str(node_name))

    mdi.MDI_Send_Command("<KE", comm)
    ke = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
    print("   KE: " + str(ke))

    #mdi.MDI_Send_Command("<PE", comm)
    #pe = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
    #print("   PE: " + str(pe))

    mdi.MDI_Send_Command("<FORCES", comm)
    forces = mdi.MDI_Recv(3 * natoms, mdi.MDI_DOUBLE, comm)
#    print("   FORCES: " + str(forces))

    #forces = [ 0.0 for i in range(3*natoms) ]
    mdi.MDI_Send_Command(">FORCES", comm)
    mdi.MDI_Send(forces, 3 * natoms, mdi.MDI_DOUBLE, comm)
    
    mdi.MDI_Send_Command("<VELOCITIES", comm)
    velocities = mdi.MDI_Recv(3 * natoms, mdi.MDI_DOUBLE, comm)
    #print("   VELOCITIES: " + str(velocities))
    
#    velocities = [ 0.0 for i in range(3*natoms) ]
    mdi.MDI_Send_Command(">VELOCITIES", comm)
    mdi.MDI_Send(velocities, 3 * natoms, mdi.MDI_DOUBLE, comm)
    


#mdi.MDI_Send_Command("@INIT_MD", comm)
#for i in range(100):
#    mdi.MDI_Send_Command("@", comm)

#mdi.MDI_Send_Command("<CELL", comm)
#cell = mdi.MDI_Recv(9, mdi.MDI_DOUBLE, comm)
#print("Cell: " + str(cell))

#mdi.MDI_Send_Command("<CELL_DISPL", comm)
#cell_displ = mdi.MDI_Recv(3, mdi.MDI_DOUBLE, comm)
#print("Cell_displ: " + str(cell_displ))

#mdi.MDI_Send_Command("<PE", comm)
#pe = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
#print("PE: " + str(pe))

#mdi.MDI_Send_Command("<KE", comm)
#ke = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
#print("KE: " + str(ke))

print("CCC")

mdi.MDI_Send_Command("EXIT", comm)
