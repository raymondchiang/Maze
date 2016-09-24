# Maze
A python maze game in terminal.

## Level File Format
At the header of the file:
```
@size=(10,10)
@name=Level 1
@viewfield=1
```

#### Symbol
- ` ` for road
- `$` for wall
- **`P`** layer
- **`G`** ate
- **`K`** ey
- **`E`** nd

#### Example
```
@size=(10,10)
@name=Level 1
@viewfield=1

P $$$$$$ $;
$ +      $;
  $ $$$$  ;
 $$    $ $;
  $ $$   $;
$ $$$$$$ $;
$      $  ;
  $ $$ $$ ;
 $$ $$$$$ ;
 $     E$ ;
```


## Todo
- [x] Classify
- [x] Level loader
- [ ] Gate & Key
- [x] Start Menu
- [ ] Portals
