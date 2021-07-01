#!/bin/bash
git clone https://github.com/sstephenson/bats /usr/local/bats

## Simple test
#!/usr/bin/env /usr/local/bats

@test "addition using bc" {
  result="$(echo 2+2 | bc)"
  [ "$result" -eq 4 ]
}

@test "addition using dc" {
  result="$(echo 2 2+p | dc)"
  [ "$result" -eq 4 ]
}
