set source_path=%1
set target_path=%2
set inter_dir=inter_ensemble
set root_dir=save

python -m squad.prepro --mode single --single_path %source_path% --target_dir %inter_dir% --glove_dir .

set eargs=
for num in 31 33 34 35 36 37 40 41 43 44 45 46; do
    set load_path=%root_dir%/%num%/save
    shared_path=%root_dir%/%num%/shared.json
    eval_path=%inter_dir%/eval-%num%.pklz
    eargs=%eargs% %eval_path%
    python -m basic.cli --data_dir %inter_dir% --eval_path %eval_path% --nodump_answer --load_path %load_path% --shared_path %shared_path% --eval_num_batches 0 --mode forward --batch_size 1 --len_opt --cluster --cpu_opt --load_ema
done
wait

python -m basic.ensemble --data_path %inter_dir%/data_single.json --shared_path %inter_dir%/shared_single.json -o %target_path% %eargs%
