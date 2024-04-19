//split.cpp
#include <cctype>
#include<string>
#include<vector>
#include<iostream>

using namespace std;

vector<string> split(const string& s) {
	vector<string> ret;
	typedef string::size_type string_size;
	string_size i = 0;

	//�Һ���: ���ݱ��� [������ i , ������ i) ������ �ִ�
	while (i != s.size()) {
		//�����ϴ� ������� ����
		//�Һ���: ���ݱ��� [������ i , ������ i) ������ �ִ�
		//���ڵ��� ��� ����
		while (i != s.size() && isspace(s[i])) {
			++i;
		}
		//������ ���� �ܾ��� ���� ã��
		string_size j = i;
		while (j != s.size() && !isspace(s[j])) {
			j++;
		}


		//������ �ƴ� ���ڵ��� ã���� ��
		if (i != j) {
			//i�������� j-i���� ���ڵ��� s�� ����
			ret.push_back(s.substr(i, j - i));
			i = j;
		}
	}
	return ret;
}

int main() {
	string s;

	while (getline(cin, s)) {
		vector<string> v = split(s);

		//���� v�� ������ �ܾ ���� ���
		for (vector<string>::size_type i = 0; i != v.size(); i++) {
			cout << v[i] << endl;
		}
	}
}