set source_path=%1
set target_path=%2
set inter_dir=inter_single
set root_dir=save

python -m squad.prepro --mode single --single_path %source_path% --target_dir %inter_dir% --glove_dir .

set num=37
set load_path="%root_dir%/%num%/save"
set shared_path="%root_dir%/%num%/shared.json"
set eval_path="%inter_dir%/eval.pklz"
python -m basic.cli --data_dir %inter_dir% --eval_path %eval_path% --nodump_answer --load_path %load_path% --shared_path %shared_path% --eval_num_batches 0 --mode forward --batch_size 1 --len_opt --cluster --cpu_opt --load_ema

python -m basic.ensemble --data_path %inter_dir%/data_single.json --shared_path %inter_dir%/shared_single.json -o %target_path% %eval_path%


