function [i] = Mandelbrot(jx,ix)
  complex = jx + ix*1i;
  history = [jx ix];
  for i = 1:200
    new = (history(end,1)+(history(end,2)*1i))^2;
    if (real(new) == Inf || imag(new) == Inf)
      break
    else
      history(end+1,:) = [real(new) imag(new)];
    endif
  end
endfunction