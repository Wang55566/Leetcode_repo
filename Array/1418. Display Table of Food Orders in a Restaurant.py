class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        displaying_table = {}
        table_header = []
        res = []

        for order in orders:
            table_n = order[1]
            item = order[2]
            if item not in table_header:
                table_header.append(item)

            if table_n not in displaying_table:
                displaying_table[table_n] = {item:1}
            else:
                if item in displaying_table[table_n]:
                    displaying_table[table_n][item] +=1
                else:
                    displaying_table[table_n][item] =1

        sorted_displaying_table = dict(sorted(displaying_table.items(), key=lambda x: int(x[0])))

        table_header.sort()

        res.append(["Table"] + table_header)

        for table_no in sorted_displaying_table:
            order_table = [table_no]
            for i in range(len(table_header)):
                if table_header[i] not in sorted_displaying_table[table_no]:
                    order_table.append(str(0))
                else:
                    order_table.append(str(sorted_displaying_table[table_no][table_header[i]]))
            res.append(order_table)


        return res
