### Structure

f(idx, []):
    if idx >= n:
        print([])
        ans.append([:])
        return
    # Take
    [].add(arr[idx])
    f(idx+1, [])

    # Not
    [].remove(arr[idx])
    f(idx+1, [])


Note: Do not copy the reference when appending to answer list, just copy values.
