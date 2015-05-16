# ngpm
Angular Package Manager for angular-browserify-lessc (ABL) modules.


## install
```
sudo pip install git+https://github.com/7yl4r/ngpm
```

## usage
### add/remove abl modules

* install the [ng-library of abl modules](https://github.com/7yl4r/ng-library) as submodule of your repo
* use ngpm to install what you want (see `ngpm --help`)

## creating modules
`ngpm new` will set up boilerplate for a new module, but there is some additional information you need to know:

* use the 'abl-dependencies' attribute in `package.json` to specify dependence on another abl package.
