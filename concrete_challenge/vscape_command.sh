# init environment
rm -rf /tmp/coop.out.*
rm -rf /home/vscape/input_cooplus/*
rm /home/vscape/cooplusmotivation/concrete_challenge/chall

# compile and info collection
clang++ -O0 /home/vscape/cooplusmotivation/concrete_challenge/chall.cpp -o /home/vscape/cooplusmotivation/concrete_challenge/chall -Xclang -fdump-verbose -Xclang -fdump-eachlayout -Xclang -fdump-ckx -fsanitize=cfi -fvisibility=hidden -flto   -L`jemalloc-config --libdir` -Wl,-rpath,`jemalloc-config --libdir` -ljemalloc `jemalloc-config --libs`
cp /tmp/coop.out.* /home/vscape/input_cooplus/

# vscape analyzing
cd /home/vscape/vscape
# delete old database
python clear_database.py

# build new database
python build_collection1.py
python build_collection2.py
python build_collection3.py
python delete_repeated_fast.py


# primitive filtering 
python add_childs.py
python build_whitelist.py
python step1_vcallsite_filter.py
python delete_other_oob.py
python step2_vcallsite_filter.py
python step3_.py
python step4_.py
python step5_.py
python step6_.py
python step7_.py
python step8_.py
python step9_.py
python step10_.py


cd for_motivation_case
# primitive pair inference
python relayobjectinfo.py

# auto pwn
cd /home/vscape/cooplusmotivation/concrete_challenge
python autogen.py