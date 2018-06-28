-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2018 年 06 月 21 日 12:37
-- 服务器版本: 5.5.53
-- PHP 版本: 5.4.45

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `sports_meeting`
--

-- --------------------------------------------------------

--
-- 表的结构 `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` char(16) NOT NULL,
  `password` char(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- 转存表中的数据 `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'root', 'root'),
(2, 'admin', 'admin');

-- --------------------------------------------------------

--
-- 表的结构 `pc`
--

CREATE TABLE IF NOT EXISTS `pc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(16) NOT NULL,
  `upid` int(16) NOT NULL,
  `cj` int(8) DEFAULT NULL,
  `sh` int(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=19 ;

--
-- 转存表中的数据 `pc`
--

INSERT INTO `pc` (`id`, `uid`, `upid`, `cj`, `sh`) VALUES
(3, 15730133, 10000002, NULL, 0),
(1, 15730133, 10000003, NULL, 0),
(12, 15730133, 10000001, 87, 1),
(14, 20180101, 10000001, NULL, 0),
(15, 20180101, 10000002, NULL, 0),
(17, 20180101, 10000006, 55, 1),
(18, 15730133, 10000005, 99, 1);

-- --------------------------------------------------------

--
-- 表的结构 `project`
--

CREATE TABLE IF NOT EXISTS `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(16) NOT NULL,
  `pname` char(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- 转存表中的数据 `project`
--

INSERT INTO `project` (`id`, `pid`, `pname`) VALUES
(1, 10000001, '1000米'),
(2, 10000002, '100米'),
(3, 10000003, '跳远'),
(4, 10000004, '跳高'),
(5, 10000005, '4x100接力'),
(6, 10000006, '铅球');

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(16) NOT NULL,
  `sname` char(8) NOT NULL,
  `szy` char(32) NOT NULL,
  `spw` char(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `student`
--

INSERT INTO `student` (`id`, `sid`, `sname`, `szy`, `spw`) VALUES
(1, 15730133, '赵健', '计算机科学与技术一班', '15730133'),
(2, 15730134, '张奥', '计算机科学与技术一班', '15730134');

-- --------------------------------------------------------

--
-- 表的结构 `teacher`
--

CREATE TABLE IF NOT EXISTS `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(16) NOT NULL,
  `tname` char(8) NOT NULL,
  `tpw` char(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `teacher`
--

INSERT INTO `teacher` (`id`, `tid`, `tname`, `tpw`) VALUES
(1, 20180101, '张凯', '20180101'),
(2, 20180102, '张昭', '20180102');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
