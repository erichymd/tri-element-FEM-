import numpy as np

young=10.
poisson=0.001
d11=young/(1-poisson*poisson)
d12=young*poisson/(1-poisson*poisson)
d13=0.0
d21=d12
d22=young/(1-poisson*poisson)
d23=0.0
d31=d13
d32=d23
d33=((1-poisson)/2)*(young/(1-poisson*poisson))
list_d1 = [d11,d12,d13]
list_d2 = [d21,d22,d23]
list_d3 = [d31,d32,d33]
D=np.array([list_d1,list_d2,list_d3])

print("D")
print(D)
nx=[0]*5
ny=[0]*5
nz=[0]*5
nex=[0]*4
ney=[0]*4
nez=[0]*4
ele_num_node_i=[0]*5
ele_num_node_j=[0]*5
ele_num_node_k=[0]*5
dofnum=[0]*8

totalNodeNum=4
KT=np.zeros((totalNodeNum*2,totalNodeNum*2))
LV=(np.zeros(totalNodeNum*2))
nx[1]=0.
ny[1]=0.
nz[1]=0.
nx[2]=1.
ny[2]=0.
nz[2]=0.
nx[3]=0.
ny[3]=1.
nz[3]=0.
nx[4]=1.
ny[4]=1.
nz[4]=0.
ele_num_node_i[1]=1
ele_num_node_j[1]=2
ele_num_node_k[1]=3
ele_num_node_i[2]=2
ele_num_node_j[2]=4
ele_num_node_k[2]=3

fix=4
constraint_node=[0]*fix
constraint_dir=[0]*fix
constraint_dof=[0]*fix

num_force=2
force_node=[0]*num_force
force_dir=[0]*num_force
force_dof=[0]*num_force
force_force=[0]*num_force



constraint_node[0]=1
constraint_dir[0]=0
constraint_node[1]=1
constraint_dir[1]=1
constraint_node[2]=2
constraint_dir[2]=1
constraint_node[3]=3
constraint_dir[3]=0

force_node[0]=2
force_dir[0]=0
force_force[0]=500.
force_node[1]=4
force_dir[1]=0
force_force[1]=500.
i=0
for i in range(num_force) :
    force_dof=force_node[i]*2-2+force_dir[i]
    print(force_dof)
    LV[force_dof]=force_force[i]
    print(force_node)
    print(LV)

for i in range(2) :

    nex[1]=nx[ele_num_node_i[i+1]]
    ney[1]=ny[ele_num_node_i[i+1]]
    nez[1]=nz[ele_num_node_i[i+1]]
    nex[2]=nx[ele_num_node_j[i+1]]
    ney[2]=ny[ele_num_node_j[i+1]]
    nez[2]=nz[ele_num_node_j[i+1]]
    nex[3]=nx[ele_num_node_k[i+1]]
    ney[3]=ny[ele_num_node_k[i+1]]
    nez[3]=nz[ele_num_node_k[i+1]]

    delta=((nex[2]-nex[1])*(ney[3]-ney[1])-(nex[3]-nex[1])*(ney[2]-ney[1]))
    b11=ney[2]-ney[3]

    b12=0.0
    b13=ney[3]-ney[1]
    b14=0.0
    b15=ney[1]-ney[2]
    b16=0.0

    b21=0.0
    b22=nex[3]-nex[2]
    b23=0.0
    b24=nex[1]-nex[3]
    b25=0.0
    b26=nex[2]-nex[1]

    b31=nex[3]-nex[2]
    b32=ney[2]-ney[3]
    b33=nex[1]-nex[3]
    b34=ney[3]-ney[1]
    b35=nex[2]-nex[1]
    b36=ney[1]-ney[2]

    list_b1=[b11,b12,b13,b14,b15,b16]
    list_b2=[b21,b22,b23,b24,b25,b26]
    list_b3=[b31,b32,b33,b34,b35,b36]

    B=np.array([list_b1,list_b2,list_b3])
    print("B")
    print(B)

    Bt=np.transpose(B)
    print("Bt")
    print(Bt)
    KE=np.dot(Bt,D)
    print("KE1")
    print(KE)
    KE=np.dot(KE,B)
    print("KE2")
    print(KE)
    S=0.5*abs((nex[1]-nex[3])*(ney[2]-ney[3])-(nex[2]-nex[3])*(ney[1]-ney[3]))
    h=1.0
    KE=S*h*KE
#    print(KE)

    dofnum[0]=ele_num_node_i[i+1]*2-2
    dofnum[1]=ele_num_node_i[i+1]*2-1
    dofnum[2]=ele_num_node_j[i+1]*2-2
    dofnum[3]=ele_num_node_j[i+1]*2-1
    dofnum[4]=ele_num_node_k[i+1]*2-2
    dofnum[5]=ele_num_node_k[i+1]*2-1

    print("dof")
    print(dofnum)
    print("KE=")
    print(KE)
    for dofnumi1 in range(6) :
        for dofnumi2 in range(6) :
            KT[dofnum[dofnumi1]][dofnum[dofnumi2]]=KT[dofnum[dofnumi1]][dofnum[dofnumi2]]+KE[dofnumi1][dofnumi2]
#KT[dofnum[0]][dofnum[0]]=KT[dofnum[0]][dofnum[0]]+KE[0][0]
#KT[dofnum[1]][dofnum[0]]=KT[dofnum[1]][dofnum[0]]+KE[1][0]
#KT[dofnum[0]][dofnum[1]]=KT[dofnum[0]][dofnum[1]]+KE[0][1]
#KT[dofnum[1]][dofnum[1]]=KT[dofnum[1]][dofnum[1]]+KE[1][1]

#print(KT)

#for i in range(fix*2) :
#constraint_dof[i]=constraint[i][0]-1+constraint[i][1]
#constraint_dof[0]=constraint_node[0]*2-2+constraint_dir[0]
#constraint_dof[1]=constraint_node[1]*2-2+constraint_dir[1]
#constraint_dof[2]=constraint_node[2]*2-2+constraint_dir[2]
#constraint_dof[3]=constraint_node[3]*2-2+constraint_dir[3]

print("before")
print(KT)
for i in range(fix,0,-1):
    KT=np.delete(KT,constraint_dof[0],0)
    KT=np.delete(KT,constraint_dof[0],1)
print("after")
print(KT)

print(constraint_dof)
#print(LV)
