import polars as pl
import numpy as np

def solution(input_df: pl.DataFrame):
    input_df = input_df.select(pl.all().replace({'.': 0, '@': 1}).cast(int))
    input_np = input_df.to_numpy()
    final_df = np.pad(input_np, pad_width=1, mode='constant', constant_values=0)

    old_result = -1
    result = 0

    while result != old_result:
        old_result = result
        mask = np.zeros_like(final_df)

        for i in range(0, input_df.shape[0]):
            for j in range(0, input_df.shape[1]):
                check_arr = final_df[i:i + 3, j:j + 3]

                if check_arr[1,1] == 0:
                    continue

                if check_arr.flatten().sum() - 1 < 4:
                    result += 1
                    mask[i + 1,j+1] = 1
        np.putmask(final_df, mask, 0)
    return result

if __name__ == '__main__':
    input_str = []
    with open('../input.txt') as f:
        lines = f.readlines()
        for line in lines:
            input_str.append(list(line.strip()))

    df = pl.DataFrame(input_str)

    print(solution(df))
