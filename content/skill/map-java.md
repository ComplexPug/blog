---
title: 'Map Java源码分析'
date: 2024-04-17T21:03:44+08:00
draft: false
description: '' 
weight: 0 # 默认0最小，其他的按照0从小到大展示优先级递增，
tags: [] # 
author: "ComplexPug"
hidemeta: false # 时间，作者等隐藏信息
---
被拷打了。
## HashMap
### 介绍
基于Hash Table实现的Map。允许null key和null value。不同步。无序。
是不同步的(Collections.synchronizedMap可以同步但没必要)。
在代码的开始有这么一段。
```java
 /*
     * Implementation notes.
     *
     * This map usually acts as a binned (bucketed) hash table, but
     * when bins g......
```
### 初始了解
大概就是数组+链表+红黑树的一个简单hash table。
数组长度是pow of two的。
```
- - - - - - - - - - - 
*		  *
*		 / \
*       *   *
```
### 一些常数
```java
static final int DEFAULT_INITIAL_CAPACITY = 1 << 4; // aka 16
static final int MAXIMUM_CAPACITY = 1 << 30;
static final float DEFAULT_LOAD_FACTOR = 0.75f;
static final int TREEIFY_THRESHOLD = 8;
static final int UNTREEIFY_THRESHOLD = 6;
static final int MIN_TREEIFY_CAPACITY = 64;//容量为64的时候bucket才会有机会转化为红黑树
```

### 为什么TREEIFY_THRESHOLD(转化为红黑树的阈值)默认为8
在源码里已经说明了，hash的分布近似于泊松分布。  
（默认情况下）出现一个长度大于8的TreeNode的概率是十万分之一。  
这一段换很有意思。他说在默认情况下(0.75)的节点平均会存储0.5个Value。  
一般人可能会直接算0.75/1,或者根e本不会理睬为什么是这样。  
相当于积分($$\int_{1}^{2} \frac{0.75}{x} d_x$$)了一下。从(0.75,2)到(0.75,1)。虽说并不是很妙，但总归很细节。  
```java
 * Because TreeNodes are about twice the size of regular nodes, we
 * use them only when bins contain enough nodes to warrant use
 * (see TREEIFY_THRESHOLD). And when they become too small (due to
 * removal or resizing) they are converted back to plain bins.  In
 * usages with well-distributed user hashCodes, tree bins are
 * rarely used.  Ideally, under random hashCodes, the frequency of
 * nodes in bins follows a Poisson distribution
 * (http://en.wikipedia.org/wiki/Poisson_distribution) with a
 * parameter of about 0.5 on average for the default resizing
 * threshold of 0.75, although with a large variance because of
 * resizing granularity. Ignoring variance, the expected
 * occurrences of list size k are (exp(-0.5) * pow(0.5, k) /
 * factorial(k)). The first values are:
* 0:    0.60653066
* 1:    0.30326533
* 2:    0.07581633
* 3:    0.01263606
* 4:    0.00157952
* 5:    0.00015795
* 6:    0.00001316
* 7:    0.00000094
* 8:    0.00000006
* more: less than 1 in ten million
```
## TreeMap
## HashTable
## LinkedHashMap

## 对比
