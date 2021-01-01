#coding:utf-8
from jinja2 import Template
import random
from genTree import generate_tree


# temp = open("challenge.cpp.temp").read()
# # name = input("Enter your name: ")
# tm = Template(temp)
# msg = tm.render(subclasses_declare="cccc"*88)
# print(msg)
# idx, parent_idx , prefix_buf_size，suffix_buf_size
template_subclasses_declare=u'''
class shape{{idx}}: public shape{{parent_idx}}{
    public:
        virtual void render(void);
        char prefix_buf[{{prefix_buf_size}}];
        unsigned long long param_{{idx}};
        char suffix_buf[{{suffix_buf_size}}];
}; 
'''
# idx
template_rewrite_vfunc=u'''
void shape{{idx}}::render(){
    param_{{idx}} = param_0;
};
'''

def random_factory():
    max = 20
    return random.randint(0,20)

def generate_code(idx,parent_idx):
    decl = Template(template_subclasses_declare)
    concrete_decl=decl.render(idx=idx,
    parent_idx=parent_idx,
    prefix_buf_size=random_factory(),
    suffix_buf_size=random_factory())
    vfunc = Template(template_rewrite_vfunc)
    concrete_vfunc=vfunc.render(idx=idx)
    return concrete_decl+concrete_vfunc
    
    pass

def pppp(idx):
    print(idx)


def generate_declares_for_all_nodes(G):
    content = ''
    for n in G.iternodes():
        alist=G.predecessors(n)
        if len(alist)==0:
            parent_idx=0
        elif len(alist) == 1:
            parent_node=alist[0]
            parent_idx = parent_node
        else:
            print (alist)
            print(parent_node)
            raise Exception("wrong pred > 1")
        idx=n
        content+=generate_code(idx,parent_idx)

    return content





if __name__ =="__main__":
    nodenum = 35
    G,root=generate_tree(nodenum)
    c=generate_declares_for_all_nodes(G)

    temp = open("challenge.cpp.temp").read()
# # name = input("Enter your name: ")
    tm = Template(temp)
    msg = tm.render(nodenum=nodenum,
    subclasses_declare=c,
    banner_header_size=32,
    vul_obj_size = 160,
    vul_read_in_size = 178,
    )
    print(msg)
    ff = open("challenge.cpp","w")
    ff.write(msg)
    ff.close()

    