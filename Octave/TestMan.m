function history = TestMan
  a = [-10:0.1:10];
  b = [-10:0.1:10];

  [p,q] = meshgrid(a,b);

  pairs = [p(:) q(:)];
  total = length(pairs)
  for x =  1:total,
    jx = pairs(x,1);
    ix = pairs(x,2);
    i = Mandelbrot(jx,ix);
    history(end+1,:) = [jx ix i];
    display(["Progress: " , num2str((x/total)*100),"%"])
  endfor
  history (:,3) = history(:,3) / norm(history(:,3));
endfunction