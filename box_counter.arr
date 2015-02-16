data Box:
  | box(ref v)
end

fun mk-counter():
  ctr = box(0)
  lam():
    ctr!{v : (ctr!v + 1)}
    ctr!v
  end
end



