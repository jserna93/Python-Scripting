reverse_list([], []).
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, TailReversed),
    append(TailReversed, [Head], Reversed).

main :-

    read(InputList),
    reverse_list(InputList, ReversedList),
    write(ReversedList),nl.
