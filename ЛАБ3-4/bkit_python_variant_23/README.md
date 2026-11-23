# БКИТ — лабораторная работа № 3–4, вариант 23

В [методичке](https://github.com/ugapanyuk/BKIT_2022/wiki/lab_python_fp) для этой работы приведены семь общих задач без разбивки по вариантам. В проекте выполнены все семь задач. Требуется Python 3.8 или новее; сторонние зависимости не нужны.

Распакуйте архив и выполните команды из каталога, где лежит этот README:

```sh
python3 -m lab_python_fp.field
python3 -m lab_python_fp.gen_random
python3 -m lab_python_fp.unique
python3 -m lab_python_fp.sort
python3 -m lab_python_fp.print_result
python3 -m lab_python_fp.cm_timer
python3 -m lab_python_fp.process_data data_demo.json
python3 -m unittest -v
```

`data_demo.json` — контрольная выборка, на которой сделан прогон для отчёта. Для прогона на наборе из методички скачайте [data_light.json](https://github.com/ugapanyuk/BKIT_2021/blob/main/notebooks/fp/files/data_light.json) (Download raw file), положите рядом с README и запустите:

```sh
python3 -m lab_python_fp.process_data data_light.json
```

Суммы зарплат и показания таймера могут различаться между запусками.
