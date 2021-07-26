/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : newday

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2021-07-26 17:06:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bank_user
-- ----------------------------
DROP TABLE IF EXISTS `bank_user`;
CREATE TABLE `bank_user` (
  `account` varchar(100) COLLATE utf8_bin NOT NULL,
  `username` varchar(20) COLLATE utf8_bin NOT NULL,
  `password` varchar(20) COLLATE utf8_bin NOT NULL,
  `country` varchar(20) COLLATE utf8_bin NOT NULL,
  `province` varchar(20) COLLATE utf8_bin NOT NULL,
  `street` varchar(20) COLLATE utf8_bin NOT NULL,
  `door` varchar(20) COLLATE utf8_bin NOT NULL,
  `money` float(20,2) NOT NULL,
  `registerDate` datetime NOT NULL,
  `bankname` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of bank_user
-- ----------------------------
INSERT INTO `bank_user` VALUES ('11000', '大佬', '123456', '中国', '北京', '沟里', '110', '10000001.00', '2021-07-19 15:31:47', '中国人民银行');
INSERT INTO `bank_user` VALUES ('73647629', 'zxc', 'asd', 'zxc', 'zxc', 'zxc', 'zxc', '98.00', '2021-07-26 16:50:48', '中国工商银行昌平回龙观支行');
