-module(test).

-export([init/0,id/1,type/1,timestamp/0,init1/0]).

init() ->
  application:start(bson),
  application:start(crypto),
  application:start(mongodb),

  Host = "114.119.6.150",
  Port = 27017,
  Database = <<"db0">>,
  Collection = <<"TopicHistory">>,
  
  UserId = 10087,
  Nickname = unicode:characters_to_binary("回家吃饭"),
  Body = unicode:characters_to_binary("曹大爷操蛋......"),
  Map1 = #{
    <<"type">> => 1,			%%	
    <<"userId">> => 10086,		%%
    <<"id">> => <<"USER/10089">>,	%%
    <<"name">> => Nickname,		%%
    <<"desc">> => Body,			%%
    <<"time">> => 11860056656,	%%
    <<"count">> => 198			%%
  },
  
  {ok, Connection} = mongo:connect([{database, Database}, {host, Host}, {port, Port}]),
  Record = mongo:find_one(Connection, Collection, {<<"_id">>, UserId}),
  case maps:size(Record) of
    0 ->
      Map2 = #{<<"_id">> => UserId, <<"topics">> => [Map1]},
      mongo:insert(Connection, Collection, Map2);
    _ ->
      Q = #{<<"_id">> => UserId},
	  Ops = #{<<"$addToSet">> => #{<<"topics">> =>  #{<<"$each">> => [Map1]}}},
	  mongo:update(Connection, Collection, Q, Ops)
  end.

init1()->
  Host = "114.119.6.150",
  Port = 27017,
  Database = <<"db0">>,
  Collection = <<"TopicHistory">>,
  UserId = 10087,
  Id = "USER/10089",
  
  {ok, Connection} = mongo:connect([{database, Database}, {host, Host}, {port, Port}]),
  Record = mongo:find_one(Connection, Collection, {<<"_id">>, UserId, <<"topics.id">>, Id}),
  Record.
	
%% 获取用户Id
id(Topic) ->
	Index = string:chr(Topic, 47),
	string:substr(Topic, Index + 1).

%% 获取主题类型
type(Topic) ->
	Index = string:chr(Topic, 47),
	case string:substr(Topic, 1, Index - 1) of
		"USER" -> 1;
		"GROUP" -> 2;
		"SYSTEM" -> 3;
		_ -> 0
	end.

%% 获取当前时间秒数
timestamp() -> 
  {M, S, _} = os:timestamp(),
  M * 1000000 + S.

