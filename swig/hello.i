%module hello

%{
#include <stdlib.h>
#include "hellomodule.h"
%}

%include "hellomodule.h"
