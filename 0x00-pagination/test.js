const dataset = [
  { id: 1, name: "John" },
  { id: 2, name: "Jane" },
  { id: 3, name: "Bob" },
  { id: 4, name: "Alice" },
  { id: 5, name: "Mark" },
  { id: 6, name: "Mary" },
  { id: 7, name: "Tom" },
  { id: 8, name: "Sara" },
  { id: 9, name: "Mike" },
  { id: 10, name: "Linda" },
  { id: 11, name: "David" },
  { id: 12, name: "Emily" },
  { id: 13, name: "Jack" },
  { id: 14, name: "Amy" },
  { id: 15, name: "Kate" },
];

function pagination(dataset, page = 1, page_size = 5) {
  // calculate the total number of items in dataset
  const total_items = dataset.length;
  // cal the total num of pages
  const num_pages = Math.ceil(total_items / page_size);
  // cal the indices of the start and end page
  const start_idx = (page - 1) * page_size;
  const end_idx = page_size + start_idx;

  // retrieve items for the current page
  const items = dataset.slice(start_idx, end_idx);
  return { page, page_size, total_items, num_pages, items };

}
const trial = pagination(dataset, 3, 5);
console.log(trial)
